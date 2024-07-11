package com.realizar_test_service.realizar_test_service.model.model_temporal;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

import java.util.List;

public class RangoSeccion {

    private Integer idRangoSeccion;
    private Integer idSeccion; // Referencia a la Seccion
    private Integer minimo;
    private Integer maximo;
    private String diagnostico;

    // Constructor, getters y setters

    public RangoSeccion() {
    }

    public RangoSeccion(Integer idRangoSeccion, Integer idSeccion, Integer minimo, Integer maximo, String diagnostico) {
        this.idRangoSeccion = idRangoSeccion;
        this.idSeccion = idSeccion;
        this.minimo = minimo;
        this.maximo = maximo;
        this.diagnostico = diagnostico;
    }

    public Integer getIdRangoSeccion() {
        return idRangoSeccion;
    }

    public void setIdRangoSeccion(Integer idRangoSeccion) {
        this.idRangoSeccion = idRangoSeccion;
    }

    public Integer getIdSeccion() {
        return idSeccion;
    }

    public void setIdSeccion(Integer idSeccion) {
        this.idSeccion = idSeccion;
    }

    public Integer getMinimo() {
        return minimo;
    }

    public void setMinimo(Integer minimo) {
        this.minimo = minimo;
    }

    public Integer getMaximo() {
        return maximo;
    }

    public void setMaximo(Integer maximo) {
        this.maximo = maximo;
    }

    public String getDiagnostico() {
        return diagnostico;
    }

    public void setDiagnostico(String diagnostico) {
        this.diagnostico = diagnostico;
    }

}
