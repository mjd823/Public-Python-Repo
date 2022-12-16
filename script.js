const form = document.getElementById('form');
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values of the 'interests' and 'skills' inputs
  const interests = document.getElementById('interests').value;
  const skills = document.getElementById('skills').value;

  // Construct a JavaScript object with the values
  const data = { interests, skills };

  // Send an HTTP POST request to the Python script with the data as the request body
  fetch('https://mjd823.github.io/Public-Python-Repo/script.py', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    // When the response is received, parse it as JSON
    .then((response) => response.json())
    // Update the 'results' element with the data
    .then((data) => {
      const results = document.getElementById('results');
      results.innerHTML = `<p>${data}</p>`;
    });
});
