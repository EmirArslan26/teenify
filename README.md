# Teenify

Teenify is a playful tool that converts plain Turkish text into exaggerated teen slang. It repeats vowels and appends a signature suffix to give any sentence a humorous, youthful tone. You can use Teenify as a command-line tool or integrate it into your own Python code, and there's even a simple API powered by FastAPI.

## Features

- **CLI:** Convert text straight from your terminal.
- **Python API:** Import `teenify` in your own projects.
- **FastAPI server:** Turn Teenify into a microservice.
- Zero external dependencies — works offline and runs anywhere.

## Installation

Clone the repository and install Teenify in editable mode:

```bash
git clone https://github.com/EmirArslan26/teenify.git
cd teenify
pip install -e .
```

## Usage

### CLI

```bash
python -m teenify.cli "Bugün derse gelmiyorum, kanka!"
# Buugüuüün deersee geelmiiyooruum, kaankaa! kanka 🤘😎
```

### Python

```python
from teenify import teenify

print(teenify("Merhaba!"))
# Meereebaa! kanka 🤘😎
```

### API

Run the API with Uvicorn:

```bash
uvicorn app.main:app --reload
```

Send a POST request to `/teenify` with JSON `{ "text": "Merhaba" }` to receive a teenified string.

## License

This project is licensed under the MIT License.

---

## Türkçe

### Teenify Nedir?

Teenify, düz Türkçe metinleri abartılı “ergen dili”ne dönüştüren eğlenceli bir araçtır. Ünlü harfleri tekrarlar ve her cümleyi sonuna kendine özgü bir ek ve emoji koyar. Teenify’ı komut satırından kullanabilir, Python projelerinize entegre edebilir veya basit bir API olarak çalıştırabilirsiniz.

### Özellikler

- **CLI:** Terminalden metin dönüştürme.
- **Python API:** `teenify` fonksiyonunu projelerinizde kullanın.
- **FastAPI sunucusu:** Teenify‑ı mikro servis olarak çalıştırın.
- Harici bağımlılık yok — çevrimdışı çalışır.

### Kurulum

Projeyi klonlayıp kurun:

```bash
git clone https://github.com/EmirArslan26/teenify.git
cd teenify
pip install -e .
```

### Kullanım

#### CLI

```bash
python -m teenify.cli "Bugün derse gelmiyorum, kanka!"
# Buugüuüün deersee geelmiiyooruum, kaankaa! kanka 🤘😎
```

#### Python

```python
from teenify import teenify

print(teenify("Merhaba!"))
# Meereebaa! kanka 🤘😎
```

#### API

Uvicorn ile API'yi çalıştırın:

```bash
uvicorn app.main:app --reload
```

`/teenify` uç noktasına `{ \"text\": \"Merhaba\" }` JSON’u ile POST atarak dönüştürülmüş metni alabilirsiniz.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
