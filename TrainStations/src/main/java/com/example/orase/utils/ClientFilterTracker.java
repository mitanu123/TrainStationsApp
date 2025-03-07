package com.example.orase.utils;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

import java.util.HashMap;
import java.util.Map;

public class ClientFilterTracker {
    private static final Map<String, SimpleIntegerProperty> filterCounts = new HashMap<>();

    public static void registerFilter(String clientId, String fromCity, String toCity) {
        String key = fromCity + "-" + toCity;
        filterCounts.putIfAbsent(key, new SimpleIntegerProperty(0));
        filterCounts.get(key).set(filterCounts.get(key).get() + 1);
    }

    public static void unregisterFilter(String clientId, String fromCity, String toCity) {
        String key = fromCity + "-" + toCity;
        if (filterCounts.containsKey(key)) {
            filterCounts.get(key).set(filterCounts.get(key).get() - 1);
            if (filterCounts.get(key).get() == 0) {
                filterCounts.remove(key);
            }
        }
    }

    public static SimpleIntegerProperty getFilterCount(String fromCity, String toCity) {
        String key = fromCity + "-" + toCity;
        return filterCounts.getOrDefault(key, new SimpleIntegerProperty(0));
    }
}