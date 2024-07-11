package com.realizar_test_service.realizar_test_service.model;
import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "historial_test")
public class HistorialTest {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer idHistorialTest;

    private Integer idUsuario;
    private Integer idTest;

    private LocalDateTime fechaRealizada;

    private String puntajes;
    private String diagnosticos;
    private String estado;

    public HistorialTest() {

    }

    public HistorialTest(Integer idUsuario, Integer idTest, LocalDateTime fechaRealizada, String puntajes, String diagnosticos, String estado) {
        this.idUsuario = idUsuario;
        this.idTest = idTest;
        this.fechaRealizada = fechaRealizada;
        this.puntajes = puntajes;
        this.diagnosticos = diagnosticos;
        this.estado = estado;
    }

    // Getters y Setters

    public Integer getIdHistorialTest() {
        return idHistorialTest;
    }

    public void setIdHistorialTest(Integer idHistorialTest) {
        this.idHistorialTest = idHistorialTest;
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

    public LocalDateTime getFechaRealizada() {
        return fechaRealizada;
    }

    public void setFechaRealizada(LocalDateTime fechaRealizada) {
        this.fechaRealizada = fechaRealizada;
    }

    public String getPuntajes() {
        return puntajes;
    }

    public void setPuntajes(String puntajes) {
        this.puntajes = puntajes;
    }

    public String getDiagnosticos() {
        return diagnosticos;
    }

    public void setDiagnosticos(String diagnosticos) {
        this.diagnosticos = diagnosticos;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
}
