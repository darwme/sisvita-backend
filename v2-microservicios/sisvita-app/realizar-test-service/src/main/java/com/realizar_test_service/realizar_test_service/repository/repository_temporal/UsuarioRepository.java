package com.realizar_test_service.realizar_test_service.repository.repository_temporal;

import com.realizar_test_service.realizar_test_service.model.model_temporal.Usuario;
import com.realizar_test_service.realizar_test_service.service.DataIntegrationService;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Repository
public class UsuarioRepository {

    static private List<Usuario> usuarios= new ArrayList<>();


    public List<Usuario> getAllUsuarios() {
        return usuarios;
    }

    public Optional<Usuario> getUsuarioById(Integer idUsuario) {
        Optional<Usuario> usuarioEncontrado = usuarios.stream()
                .filter(usuario -> idUsuario.equals(usuario.getIdUsuario()))
                .findFirst();

        if (usuarioEncontrado.isEmpty()) {
            throw new NoSuchElementException("Usuario no encontrado con id: " + idUsuario);
        }

        return usuarioEncontrado;
    }

    public Usuario saveUsuario(Usuario usuario) {
        usuarios.add(usuario);
        return usuario;
    }

    public Usuario updateUsuario(Integer idUsuario, Usuario usuario) {
        for (Usuario u : usuarios) {
            if (u.getIdUsuario().equals(idUsuario)) {
                u.setEmail(usuario.getEmail());
                u.setClave(usuario.getClave());
                u.setTipoUsuario(usuario.getTipoUsuario());
                return u;
            }
        }
        return null; // Opcional: lanzar excepción si no se encuentra el usuario
    }

    public void deleteUsuario(Integer idUsuario) {
        usuarios.removeIf(usuario -> usuario.getIdUsuario().equals(idUsuario));
    }
    public void deleteAllUsuarios() {
        usuarios.clear();
    }
}
