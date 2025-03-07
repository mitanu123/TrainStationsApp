package com.example.orase.controller;

import com.example.orase.domain.City;
import com.example.orase.service.Service;
import com.example.orase.utils.ClientFilterTracker;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public class Controller {
    @FXML
    private ComboBox<String> departureCityComboBox;
    @FXML
    private ComboBox<String> destinationCityComboBox;
    @FXML
    private CheckBox directRoutesOnlyCheckBox;
    @FXML
    private Button searchButton;
    @FXML
    private TextArea resultTextArea;
    @FXML
    private Label otherUsersLabel;

    private Service service;
    private String clientId;
    private String currentFromCity;
    private String currentToCity;

    public Controller() {
        this.clientId = UUID.randomUUID().toString();
    }

    public void setService(Service service) {
        this.service = service;
        loadCities();
    }

    private void loadCities() {
        List<String> cities = service.getAllCities();
        ObservableList<String> cityList = FXCollections.observableArrayList(cities);
        departureCityComboBox.setItems(cityList);
        destinationCityComboBox.setItems(cityList);
    }

    @FXML
    private void handleSearch() {
        String fromCityName = departureCityComboBox.getValue();
        String toCityName = destinationCityComboBox.getValue();
        boolean directOnly = directRoutesOnlyCheckBox.isSelected();

        if (fromCityName == null || fromCityName.isEmpty()) {
            resultTextArea.setText("Please select a departure city.");
            return;
        }

        if (toCityName == null || toCityName.isEmpty()) {
            resultTextArea.setText("Please select a destination city.");
            return;
        }

        Optional<City> fromCity = service.getCityByName(fromCityName);
        Optional<City> toCity = service.getCityByName(toCityName);

        if (fromCity.isPresent() && toCity.isPresent()) {
            String fromCityId = fromCity.get().getId();
            String toCityId = toCity.get().getId();
            List<String> routes = service.getRoutes(fromCityId, toCityId, directOnly);
            resultTextArea.setText(String.join("\n", routes));

            updateFilter(fromCityId, toCityId);
        } else {
            resultTextArea.setText("City not found.");
        }
    }

    private void updateFilter(String fromCity, String toCity) {
        if (currentFromCity != null && currentToCity != null) {
            ClientFilterTracker.unregisterFilter(clientId, currentFromCity, currentToCity);
        }
        currentFromCity = fromCity;
        currentToCity = toCity;
        ClientFilterTracker.registerFilter(clientId, fromCity, toCity);

        SimpleIntegerProperty countProperty = ClientFilterTracker.getFilterCount(fromCity, toCity);
        countProperty.addListener((observable, oldValue, newValue) -> updateOtherUsersLabel(newValue.intValue()));
        updateOtherUsersLabel(countProperty.get());
    }

    private void updateOtherUsersLabel(int count) {
        if (count > 1) {
            otherUsersLabel.setText((count - 1) + " other user(s) are looking at the same route");
        } else {
            otherUsersLabel.setText("");
        }
    }
}