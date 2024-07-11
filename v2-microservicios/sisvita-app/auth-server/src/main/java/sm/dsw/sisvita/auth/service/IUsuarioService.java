package sm.dsw.sisvita.auth.service;

import sm.dsw.sisvita.auth.model.Usuario;

import java.util.List;

public interface IUsuarioService {
    List<Usuario> findAll();
    Usuario findById(Long id);
    Usuario findByEmail(String email);
    void save(Usuario usuario);
    void delete(Long id);
}