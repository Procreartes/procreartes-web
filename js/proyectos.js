// Filtro de proyectos por categoría
(function () {
  "use strict";
  try {
    var botones = document.querySelectorAll(".filtros button");
    var items = document.querySelectorAll("#lista-proyectos .proyecto");
    Array.prototype.forEach.call(botones, function (b) {
      b.addEventListener("click", function () {
        var cat = b.getAttribute("data-cat");
        Array.prototype.forEach.call(botones, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        Array.prototype.forEach.call(items, function (it) { it.hidden = !!cat && it.getAttribute("data-cat") !== cat; });
      });
    });
  } catch (e) {}
})();
