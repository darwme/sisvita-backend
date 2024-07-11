package com.realizar_test_service.realizar_test_service.model;

import com.realizar_test_service.realizar_test_service.model.model_temporal.RangoSeccion;
import jakarta.persistence.*;

import java.util.Optional;

@Entity
@Table(name = "seccion_respuesta")
public class SeccionRespuesta {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer idSeccionRespuesta;

    private Integer idUsuario;
    private Integer idTest;
    private Integer idSeccion;
    private String respuestas;

    public SeccionRespuesta() {
        // Constructor vacío necesario para JPA
    }

    public SeccionRespuesta(Integer idUsuario, Integer idTest, Integer idSeccion, String respuestas) {
        this.idUsuario = idUsuario;
        this.idTest = idTest;
        this.idSeccion = idSeccion;
        this.respuestas = respuestas;
    }

    // Getters y Setters

    public Integer getIdSeccionRespuesta() {
        return idSeccionRespuesta;
    }

    public void setIdSeccionRespuesta(Integer idSeccionRespuesta) {
        this.idSeccionRespuesta = idSeccionRespuesta;
    }

    public Integer getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(Integer idUsuario) {
        this.idUsuario = idUsuario;
    }

    public Integer getIdTest() {
        return idTest;
    }

    public void setIdTest(Integer idTest) {
        this.idTest = idTest;
    }

    public Integer getIdSeccion() {
        return idSeccion;
    }

    public void setIdSeccion(Integer idSeccion) {
        this.idSeccion = idSeccion;
    }

    public String getRespuestas() {
        return respuestas;
    }

    public void setRespuestas(String respuestas) {
        this.respuestas = respuestas;
    }
}