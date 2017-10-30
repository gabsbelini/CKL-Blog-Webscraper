# CKL Backend Challenge

Esse projeto faz parte do processo seletivo da Cheesecake Labs. O objetivo dele é que o candidato crie um webscraper para extrair dados de um blog e disponibilize esses dados em forma de uma API REST.
A API está disponível nos seguintes endereços: http://45.55.255.158/articles  e http://45.55.255.158/subjects

## Bibliotecas e Ferramentas utilizadas

1. [Atom](https://atom.io/)
2. Linux Mint
3. Digital Ocean para fazer o deploy (nginx + gunicorn)
4. [YamJam](https://pypi.python.org/pypi/yamjam/): Utilizado para gerenciar dados sensíveis do arquivo `settings.py`
5. [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4): Biblioteca usada para fazer o parsing do codigo HTML da pagina e extrair as informacoes necessárias.
6. Crontab: Utilizado para agendar o job que extrai informações do site (5 em 5 minutos)
7. [Django REST Framework](https://pypi.python.org/pypi/djangorestframework): Framework utilizado para criar a API.
