package com.realizar_test_service.realizar_test_service.model.model_temporal;

public class Usuario {

    private Integer idUsuario;
    private String email;
    private String clave;
    private String tipoUsuario;

    public Usuario() {
    }

    public Usuario(Integer idUsuario, String email, String clave, String tipoUsuario) {
        this.idUsuario = idUsuario;
        this.email = email;
        this.clave = clave;
        this.tipoUsuario = tipoUsuario;
    }

    public Integer getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(Integer idUsuario) {
        this.idUsuario = idUsuario;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getClave() {
        return clave;
    }

    public void setClave(String clave) {
        this.clave = clave;
    }

    public String getTipoUsuario() {
        return tipoUsuario;
    }

    public void setTipoUsuario(String tipoUsuario) {
        this.tipoUsuario = tipoUsuario;
    }
}