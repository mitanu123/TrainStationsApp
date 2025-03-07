package com.example.orase.controller;

import com.example.orase.GUI;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;

public class MainController {

    @FXML
    private void handleOpenClientWindow(ActionEvent event) {
        GUI.clientView();
    }
}