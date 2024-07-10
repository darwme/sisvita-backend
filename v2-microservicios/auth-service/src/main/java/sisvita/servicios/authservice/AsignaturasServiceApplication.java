package sisvita.servicios.authservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.openfeign.EnableFeignClients;


@SpringBootApplication
@EnableFeignClients
public class AsignaturasServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(AsignaturasServiceApplication.class, args);
    }

}
