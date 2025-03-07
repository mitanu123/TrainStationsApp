package com.example.orase.repository;

import com.example.orase.domain.TrainStation;

import java.sql.*;
import java.util.ArrayList;
import java.util.Optional;

public class TrainStationRepository implements IRepository<String, TrainStation> {
    private final Connection connection;

    public TrainStationRepository(Connection connection) {
        this.connection = connection;
    }

    @Override
    public Optional<TrainStation> findOne(String id) {
        String sql = "SELECT * FROM train_station WHERE train_id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return Optional.of(new TrainStation(
                        rs.getString("train_id"),
                        rs.getString("departure_city_id"),
                        rs.getString("destination_city_id")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return Optional.empty();
    }

    @Override
    public Iterable<TrainStation> findAll() {
        String sql = "SELECT * FROM train_station";
        ArrayList<TrainStation> trainStations = new ArrayList<>();
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                trainStations.add(new TrainStation(
                        rs.getString("train_id"),
                        rs.getString("departure_city_id"),
                        rs.getString("destination_city_id")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return trainStations;
    }

    @Override
    public Optional<TrainStation> save(TrainStation entity) {
        String sql = "INSERT INTO train_station (train_id, departure_city_id, destination_city_id) VALUES (?, ?, ?)";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, entity.getId());
            stmt.setString(2, entity.getDepartureCityId());
            stmt.setString(3, entity.getDestinationCityId());
            stmt.executeUpdate();
            return Optional.empty();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return Optional.of(entity);
    }

    @Override
    public Optional<TrainStation> delete(String id) {
        Optional<TrainStation> trainStation = findOne(id);
        if (trainStation.isPresent()) {
            String sql = "DELETE FROM train_station WHERE train_id = ?";
            try (PreparedStatement stmt = connection.prepareStatement(sql)) {
                stmt.setString(1, id);
                stmt.executeUpdate();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return trainStation;
    }

    @Override
    public Optional<TrainStation> update(TrainStation entity) {
        String sql = "UPDATE train_station SET departure_city_id = ?, destination_city_id = ? WHERE train_id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, entity.getDepartureCityId());
            stmt.setString(2, entity.getDestinationCityId());
            stmt.setString(3, entity.getId());
            int updatedRows = stmt.executeUpdate();
            if (updatedRows > 0) {
                return Optional.empty();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return Optional.of(entity);
    }
}