package com.example.orase;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import com.example.orase.controller.Controller;
import com.example.orase.controller.MainController;
import com.example.orase.service.Service;

import java.io.IOException;
import java.util.Optional;

public class GUI extends Application {
    private static Service service;
    private static Stage stage;

    public static void setService(Service service) {
        GUI.service = service;
    }

    @Override
    public void start(Stage primaryStage) {
        GUI.stage = primaryStage;
        mainView();
        stage.show();
    }

    public static void mainView() {
        stage.setScene(createScene("main-view.fxml", Optional.empty(), MainController.class));
        stage.setTitle("Main Window");
        stage.show();
    }

    public static void clientView() {
        Stage clientStage = new Stage();
        clientStage.setScene(createScene("client-view.fxml", Optional.empty(), Controller.class));
        clientStage.setTitle("Client Window");
        clientStage.show();
    }

    private static <T> Scene createScene(String fxml, Optional<Object> parameter, Class<T> controllerClass) {
        FXMLLoader fxmlLoader = new FXMLLoader();
        fxmlLoader.setLocation(GUI.class.getResource(fxml));

        try {
            Scene scene = new Scene(fxmlLoader.load());

            T controller = fxmlLoader.getController();
            if (controller instanceof Controller) {
                ((Controller) controller).setService(service);
            }

            return scene;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void launchApp() {
        Application.launch();
    }
}