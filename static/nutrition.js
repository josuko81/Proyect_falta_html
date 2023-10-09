document.getElementById('nutritionForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const id = document.getElementById('id').value;
    const country = document.getElementById('country').value;
    const stateLgdCode = document.getElementById('stateLgdCode').value;
    const state = document.getElementById('state').value;
    const yearCode = document.getElementById('yearCode').value;
    const year = document.getElementById('year').value;
    const fromYear = document.getElementById('fromYear').value;
    const residence = document.getElementById('residence').value;
  
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
      <td>${id}</td>
      <td>${country}</td>
      <td>${stateLgdCode}</td>
      <td>${state}</td>
      <td>${yearCode}</td>
      <td>${year}</td>
      <td>${fromYear}</td>
      <td>${residence}</td>
    `;
  
    document.getElementById('nutritionTable').appendChild(newRow);
    document.getElementById('nutritionForm').reset();
  });