datos <- read.csv(file.choose())


pi_valores <- datos$Aproximacion


mean(pi_valores)

sd(pi_valores)

t.test(pi_valores)$conf.int
