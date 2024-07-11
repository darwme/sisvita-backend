package sm.dsw.sisvita.auth.service;

import org.springframework.stereotype.Service;
import sm.dsw.sisvita.auth.model.Usuario;
import sm.dsw.sisvita.auth.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

@Service
public class UsuarioService implements IUsuarioService{

    @Autowired
    private UsuarioRepository usuarioRepository;

    public List<Usuario> findAll() {
        return (List<Usuario>) usuarioRepository.findAll();
    }

    public Usuario findById(Long id_usuario) {
        return usuarioRepository.findById(id_usuario).orElse(null);
    }

    @Override
    public Usuario findByEmail(String email) {
        return null;
    }

        /*
        public Usuario findByEmail(String email) {
            return usuarioRepository.findByEmail(email);
        }
        */

    public void save(Usuario usuario) {
        usuarioRepository.save(usuario);
    }

    public void delete(Long id) {
        usuarioRepository.deleteById(id);
    }
}
