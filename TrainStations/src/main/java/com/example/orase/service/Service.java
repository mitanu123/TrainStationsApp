package com.example.orase.service;

import com.example.orase.domain.City;
import com.example.orase.domain.TrainStation;
import com.example.orase.repository.CityRepository;
import com.example.orase.repository.TrainStationRepository;
import com.example.orase.utils.Observable;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class Service extends Observable {
    private final CityRepository cityRepository;
    private final TrainStationRepository trainStationRepository;
    private static final float PRICE_PER_STATION = 10.0f;

    public Service(CityRepository cityRepository, TrainStationRepository trainStationRepository) {
        this.cityRepository = cityRepository;
        this.trainStationRepository = trainStationRepository;
    }

    public List<String> getAllCities() {
        return ((List<City>) cityRepository.findAll()).stream()
                .map(City::getName)
                .collect(Collectors.toList());
    }

    public List<String> getRoutes(String from, String to, boolean directOnly) {
        List<TrainStation> stations = (List<TrainStation>) trainStationRepository.findAll();
        List<String> routes = new ArrayList<>();

        // Find direct routes
        for (TrainStation station : stations) {
            if (station.getDepartureCityId().equals(from) && station.getDestinationCityId().equals(to)) {
                String route = getCityName(from) + " - " + station.getId() + " -> " + getCityName(to);
                float price = PRICE_PER_STATION * 1; // Direct route can have more than one station but using the same train
                routes.add(route + " | Price: " + price);
                break;
            }
        }

        if (!directOnly) {
            // Find indirect routes
            findIndirectRoutes(from, to, stations, new ArrayList<>(), routes);
        }

        return routes;
    }

    private void findIndirectRoutes(String from, String to, List<TrainStation> stations, List<String> currentRoute, List<String> routes) {
        for (TrainStation station : stations) {
            if (station.getDepartureCityId().equals(from)) {
                List<String> newRoute = new ArrayList<>(currentRoute);
                String nextCity = getCityName(station.getDestinationCityId());
                newRoute.add(getCityName(from) + " - " + station.getId() + " -> " + nextCity);
                if (station.getDestinationCityId().equals(to)) {
                    float price = PRICE_PER_STATION * newRoute.size(); // Exclude the initial station
                    routes.add(String.join(" -> ", newRoute) + " | Price: " + price);
                } else {
                    findIndirectRoutes(station.getDestinationCityId(), to, stations, newRoute, routes);
                }
            }
        }
    }

    private String getCityName(String cityId) {
        Optional<City> city = cityRepository.findOne(cityId);
        return city.map(City::getName).orElse("Unknown City");
    }

    public Optional<City> getCityByName(String name) {
        List<City> cities = (List<City>) cityRepository.findAll();
        return cities.stream().filter(city -> city.getName().equals(name)).findFirst();
    }
}