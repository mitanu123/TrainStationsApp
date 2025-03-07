package com.example.orase.domain;

public class TrainStation implements Entity<String> {
    private String trainId;
    private String departureCityId;
    private String destinationCityId;

    public TrainStation(String trainId, String departureCityId, String destinationCityId) {
        this.trainId = trainId;
        this.departureCityId = departureCityId;
        this.destinationCityId = destinationCityId;
    }

    @Override
    public String getId() {
        return trainId;
    }

    @Override
    public void setId(String trainId) {
        this.trainId = trainId;
    }

    public String getDepartureCityId() {
        return departureCityId;
    }

    public void setDepartureCityId(String departureCityId) {
        this.departureCityId = departureCityId;
    }

    public String getDestinationCityId() {
        return destinationCityId;
    }

    public void setDestinationCityId(String destinationCityId) {
        this.destinationCityId = destinationCityId;
    }
}