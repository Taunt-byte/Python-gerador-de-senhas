# Gerador de senhas em Python

Este projeto é um gerador de senhas em Python com uma interface gráfica simples. 

Ele utiliza a biblioteca Tkinter para criar uma janela onde o usuário pode especificar o tamanho desejado para a senha e gerar uma senha aleatória.

## Como funciona

- Utilizamos a biblioteca Tkinter para criar a interface gráfica.

- A janela principal é criada com o título "Gerador de Senhas".

- Em seguida, criamos os elementos da tela: um rótulo ("Tamanho da senha"), uma caixa de entrada para o usuário digitar o tamanho desejado, um botão "Gerar Senha" e um rótulo que exibirá a senha gerada.

- A função gerar_nova_senha é chamada quando o botão "Gerar Senha" é clicado. 

- Ela obtém o tamanho da senha da caixa de entrada, chama a função gerar_senha para gerar a senha aleatória e atualiza o rótulo de senha com o valor gerado.

Por fim, o loop principal janela.mainloop() é iniciado para manter a janela aberta e responder às interações do usuário.

## Rodando os testes

Para rodar os testes, rode o seguinte comando

1) Clone este repositório ou faça o download dos arquivos.
```bash
  git@github.com:Taunt-byte/Python-gerador-de-senhas.git
```

2) Execute esse comando.

```bash
  python gerador_de_senhas.py
```

## Licença

Este projeto está licenciado sob a MIT License.

[MIT](https://choosealicense.com/licenses/mit/)