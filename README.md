# Exemplo de lambda recuperando valores do AWS Secrets Manager

Pré requisitos:
- Ter um Secrets Manager criado;
- Ter o segredo inserido no Secrets Manager;
- Ter uma role com permissão para dar Get no segredo;
- Configurar o ARN do Secrets Manager na Lambda;
- Ter uma layer na lambda com a extensão para recuperação de segredos.