package sm.dsw.sisvita.auth.repository;

import org.springframework.stereotype.Repository;
import sm.dsw.sisvita.auth.model.Usuario;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

@Repository
public interface UsuarioRepository extends CrudRepository<Usuario, Long>{
    //List<Usuario> findAllByService(Long id_service);
}
