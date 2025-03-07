package com.example.orase;

import com.example.orase.repository.CityRepository;
import com.example.orase.repository.TrainStationRepository;
import com.example.orase.service.Service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) throws SQLException {
        final String url = "jdbc:postgresql://localhost:5432/Orase";
        final String user = "postgres";
        final String password = "mihai123";

        final Connection dataBaseConnection = DriverManager.getConnection(url, user, password);

        CityRepository cityRepository = new CityRepository(dataBaseConnection);
        TrainStationRepository trainStationRepository = new TrainStationRepository(dataBaseConnection);

        Service service = new Service(cityRepository, trainStationRepository);

        GUI.setService(service);
        GUI.launchApp();
    }
}