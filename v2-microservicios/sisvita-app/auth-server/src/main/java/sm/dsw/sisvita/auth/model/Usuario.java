package sm.dsw.sisvita.auth.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "usuario")
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_usuario;
    @Column(name = "email", unique = true)
    private String email;

    @Column(name = "clave")
    private String clave;

    @Column(name = "tipo_usuario")
    private String tipo_usuario;
}
