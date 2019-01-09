package org.lenskit.mooc.cbf;

import org.lenskit.data.ratings.Rating;

import javax.annotation.Nonnull;
import javax.inject.Inject;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Build a user profile from all positive ratings.
 */
public class WeightedUserProfileBuilder implements UserProfileBuilder {
    /**
     * The tag model, to get item tag vectors.
     */
    private final TFIDFModel model;

    @Inject
    public WeightedUserProfileBuilder(TFIDFModel m) {
        model = m;
    }

    @Override
    public Map<String, Double> makeUserProfile(@Nonnull List<Rating> ratings) {
        // Create a new vector over tags to accumulate the user profile
        Map<String,Double> profile = new HashMap<>();

        // TODO Normalize the user's ratings
        double ratingsSum = 0.0;
        for (Rating rating: ratings) {
            ratingsSum += rating.getValue();
        }

        double ratingsMean = ratingsSum / ratings.size();

        // TODO Build the user's weighted profile
        for (Rating rating: ratings) {
            long itemId = rating.getItemId();
            Map<String, Double> itemVector = model.getItemVector(itemId);

            double weight = rating.getValue() - ratingsMean;

            for (String attribute: itemVector.keySet()) {
                double newAttributeValue = profile.containsKey(attribute) ?
                        profile.get(attribute) + weight * itemVector.get(attribute) :
                        weight * itemVector.get(attribute);
                profile.put(attribute, newAttributeValue);
            }
        }

        // The profile is accumulated, return it.
        return profile;
    }
}
