module com.example.orase {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;


    opens com.example.orase to javafx.fxml;
    exports com.example.orase;
}