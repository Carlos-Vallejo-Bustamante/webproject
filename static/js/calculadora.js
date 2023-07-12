// Obtener los botones de la calculadora
var buttons = document.querySelectorAll('.buttons button');

// Agregar un evento de escucha para el evento de teclado
document.addEventListener('keydown', function(event) {
  // Obtener el valor de la tecla presionada
  var key = event.key;

  // Si se presiona "Enter", llamar a la función calculate()
  if (key === "Enter") {
    calculate();
    event.preventDefault();
  } else {
    // Buscar el botón correspondiente a la tecla presionada
    var button = Array.from(buttons).find(function(btn) {
      return btn.getAttribute('data-key') === key;
    });

    // Si se encuentra el botón correspondiente, simular un clic
    if (button) {
      button.click();
    }
  }
});

// Asignar eventos de clic a los botones de la calculadora
buttons.forEach(function(button) {
  button.addEventListener('click', function() {
    // Obtener el valor del botón
    var value = button.getAttribute('data-key');

    // Realizar la acción correspondiente según el valor del botón
    if (value === 'Enter') {
      calculate();
    } else if (value === 'C') {
      clearDisplay();
    } else {
      appendToDisplay(value);
    }
  });
});

function appendToDisplay(value) {
  document.getElementById('display').value += value;
}

function clearDisplay() {
  document.getElementById('display').value = '';
}

function calculate() {
  var expression = document.getElementById('display').value;
  var result = eval(expression);
  document.getElementById('display').value = result;
}
