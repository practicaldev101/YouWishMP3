# Aplicación para descargar música de YouTube

![Demo Image](https://github.com/practicaldev101/YouWishMP3/blob/main/docs/demo.png)

## Instalación
Debes seguir los siguientes pasos para poder instalar

### Windows

1. Descarga el ejecutable entrando [aquí](https://github.com/practicaldev101/YouWishMP3/releases/tag/Windows)

2. ¡Descomprimes el archivo ZIP y está listo!

#### Uso

> **Nota importante**: Desactiva cualquier antivirus. El ejecutable no tiene una licencia como tal, sin licencia se detecta como un falso positivo. Por lo que debes decirle a tus programas de protección que es confiable.

- Para usar este programa en windows, solo basta con llenar el archivo **music.txt** con las URLs de música o videos que quieres descargar.

- A continuación, ejectura el programa y saldrá una consola que te mostrará el proceso de descarga.

### Linux

1. Clona el repositorio

```
git clone https://github.com/practicaldev101/YouWishMP3.git
```

2. Accede al directorio

```
cd ./YouWishMP3/src
```

3. Instala los requerimientos manualmente.

```
pip install -r requirements.txt
```

#### Uso
Al ejecutar este comando se te creará un archivo llamado **music.txt** en caso de que no lo tengas.

```
python main.py
```

En caso de que no se cree la carpeta, crealo manualmente.

- Posteriormente, pegaras las URLs de los videos o músicas de youtube que quieres descargar en el archivo **music.txt**.

- Los archivos descargados se guardarán en la carpeta **downloads** del mismo directorio.



