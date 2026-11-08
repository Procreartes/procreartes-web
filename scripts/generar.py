#!/usr/bin/env python3
"""Genera la web de la Asociación ProCreArtes (procreartes.com).

Uso:  python3 scripts/generar.py
Datos editables (Gestor de webs del portal o a mano): data/proyectos.json
No edites los .html a mano: se sobrescriben.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from web import RAIZ, Sitio, ICO, esc, datos, mailto  # noqa: E402

CORREO = "hola@procreartes.com"

S = Sitio(
    nombre="Asociación ProCreArtes", nombre_corto="ProCreArtes",
    dominio="https://procreartes.com",
    titular="Asociación Sociocultural ProCreArtes", nif="G76307602",
    domicilio="Urbanización Villareal de Coello, 2 · 35310 Santa Brígida (Las Palmas)",
    correo=CORREO, correo_datos="protecciondatos@procreartes.com",
    objeto="Esta web informa sobre la Asociación Sociocultural ProCreArtes, sus proyectos y la forma de contactar.",
    color_tema="#1f5a88", color_fondo="#ffffff",
    precarga=["bricolage-grotesque-latin-800-normal.woff2", "figtree-latin-400-normal.woff2"],
    menu=[("/#somos", "Quiénes somos"), ("/#hacemos", "Qué hacemos"), ("/#proyectos", "Proyectos"), ("/#contacto", "Contacto")],
    marca='<span class="logo"><b>PRO</b><i>CRE</i><b>ARTES</b></span>',
    pie_html='''<div class="pie-arriba">
      <div><p class="pie-logo"><b>PRO</b><i>CRE</i><b>ARTES</b></p>
      <p>Asociación sociocultural sin ánimo de lucro · Gran Canaria</p></div>
      <div><p><a href="mailto:hola@procreartes.com">hola@procreartes.com</a></p>
      <p>Santa Brígida · Gran Canaria</p></div>
    </div>''',
)

PROYECTOS = datos("proyectos.json", [])

HACEMOS = [
    ("Juventud", "Ferias, festivales, concursos y programas de ocio para y con la gente joven."),
    ("Festivales y artes escénicas", "Creación y producción de espectáculos, muestras y festivales de calle, teatro, música y circo."),
    ("Grandes eventos", "Producción integral: permisos, planes de seguridad, técnica, montaje, logística y coordinación con las administraciones."),
    ("Campañas y comunicación", "Ideas, guion, grabación, producción y difusión de campañas institucionales y sociales."),
    ("Sostenibilidad", "Planes de sostenibilidad para festivales y eventos: residuos, agua, movilidad y huella de carbono."),
]

PRINCIPIOS = [
    "No repartimos beneficios: reinvertimos todo en proyectos sociales y culturales.",
    "La junta directiva no cobra por serlo.",
    "Trabajamos con principios democráticos, participativos y orientados a la justicia social.",
    "Nos mueve la conciencia social y colectiva, y cuidamos la responsabilidad social.",
]


def a_svg():
    """La A del logotipo, en degradado de azul marino a celeste (decorativa)."""
    return '''<svg class="a-grande" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
<defs><linearGradient id="ga" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#16406a"/><stop offset="1" stop-color="#52aad8"/></linearGradient></defs>
<path d="M100 8 192 192h-46l-46-94-46 94H8z" fill="url(#ga)"/></svg>'''


def inicio():
    hacemos = "".join(f'<li class="aparece"><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for t, d in HACEMOS)
    cats = []
    for p in PROYECTOS:
        c = p.get("categoria") or "Otros"
        if c not in cats:
            cats.append(c)
    filtros = ('<div class="filtros" role="group" aria-label="Filtrar proyectos"><button type="button" aria-pressed="true" data-cat="">Todos</button>'
               + "".join(f'<button type="button" aria-pressed="false" data-cat="{esc(c)}">{esc(c)}</button>' for c in cats) + "</div>")
    tarjetas = ""
    for p in PROYECTOS:
        enlace = p.get("enlace") or ""
        tarjetas += f'''<li class="proyecto aparece" data-cat="{esc(p.get("categoria") or "Otros")}">
      <p class="proyecto-meta"><span>{esc(p.get("categoria"))}</span>{f"<span>{esc(p['anio'])}</span>" if p.get("anio") else ""}</p>
      <h3>{esc(p.get("titulo"))}</h3><p>{esc(p.get("texto"))}</p>
      {f'<a href="{esc(enlace)}">Ver la web {ICO["flecha"]}</a>' if enlace.startswith("https://") else ""}
    </li>'''
    principios = "".join(f"<li>{ICO['check']}<span>{esc(x)}</span></li>" for x in PRINCIPIOS)
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "NGO", "name": "Asociación Sociocultural ProCreArtes",
        "alternateName": "ProCreArtes", "url": S.dominio + "/", "email": CORREO, "taxID": "G76307602", "areaServed": "Canarias",
        "address": {"@type": "PostalAddress", "streetAddress": "Urbanización Villareal de Coello, 2", "postalCode": "35310",
                    "addressLocality": "Santa Brígida", "addressCountry": "ES"},
    }, ensure_ascii=False)

    cuerpo = f'''<section class="portada">
  <div class="contenedor portada-grid">
    <div>
      <p class="antetitulo">Asociación sociocultural · Canarias</p>
      <h1>Profesionales <span class="c1">creativos</span> de las <span class="c2">artes</span>.</h1>
      <p class="entradilla">Fomentamos el desarrollo artístico y cultural con eventos, festivales, talleres y proyectos sociales, y apoyamos a artistas emergentes. Usamos el arte como herramienta de transformación.</p>
      <div class="botones">
        <a class="boton boton-azul" href="#proyectos">Ver proyectos {ICO["flecha"]}</a>
        <a class="boton boton-linea" href="#contacto">Contacto</a>
      </div>
    </div>
    <div class="portada-arte">{a_svg()}</div>
  </div>
</section>

<section class="lema" aria-label="Cómo trabajamos">
  <div class="contenedor"><p>No somos teoría, somos práctica. Una agencia de calle que se ensucia las manos: <strong>fabricamos y apenas subcontratamos</strong>.</p></div>
</section>

<section class="seccion" id="somos" aria-labelledby="t-somos">
  <div class="contenedor somos">
    <div><p class="antetitulo">Quiénes somos</p><h2 id="t-somos">Un equipo multidisciplinar, paritario y estable</h2>
    <p class="entradilla">ProCreArtes reúne a profesionales creativos de distintos sectores de las artes con un objetivo común: crecer juntos, trabajar de forma independiente y sumar en cada reto.</p>
    <p>Llevamos más de veinte años trabajando con clientes públicos y privados, festivales y grandes marcas, y contamos con colaboradores de confianza en distintas islas y especialidades.</p></div>
    <div class="principios"><h3>Una asociación sin ánimo de lucro</h3><ul class="lista-check">{principios}</ul></div>
  </div>
</section>

<section class="seccion seccion-azul" id="hacemos" aria-labelledby="t-hacemos">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Qué hacemos</p><h2 id="t-hacemos">De la idea al último tornillo</h2></div>
    <ol class="hacemos">{hacemos}</ol>
  </div>
</section>

<section class="seccion" id="proyectos" aria-labelledby="t-proyectos">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Proyectos</p><h2 id="t-proyectos">Algunos de nuestros proyectos</h2></div>
    {filtros if len(cats) > 1 else ""}
    <ul class="proyectos" id="lista-proyectos">{tarjetas}</ul>
  </div>
</section>

<section class="seccion contacto" id="contacto" aria-labelledby="t-contacto">
  <div class="contenedor contacto-caja aparece">
    <div><p class="antetitulo">Contacto</p><h2 id="t-contacto">¿Tienen un proyecto en mente?</h2>
    <p>Para propuestas, colaboraciones, artistas o administraciones, escríbannos.</p></div>
    <a class="boton boton-blanco" href="{mailto(CORREO, "Contacto desde la web")}">{ICO["mail"]} {CORREO}</a>
  </div>
</section>
<script src="/js/proyectos.js" defer></script>'''
    return S.pagina("Asociación ProCreArtes · Profesionales creativos de las artes",
                    "Asociación sociocultural sin ánimo de lucro de Canarias: festivales, artes escénicas, juventud, grandes eventos, campañas y sostenibilidad.",
                    "/", cuerpo, actual="", ld=ld)


def main():
    css = (RAIZ / "css/base.css").read_text(encoding="utf-8") + "\n" + (RAIZ / "css/tema.css").read_text(encoding="utf-8")
    S.escribir("css/estilos.css", css)
    S.publicar({"index.html": inicio()})


if __name__ == "__main__":
    main()
