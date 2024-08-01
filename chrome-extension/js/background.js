chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    fetch('http://localhost:5000/api/action', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(request)
    })
    .then(response => response.json())
    .then(data => sendResponse(data))
    .catch(error => console.error('Error:', error));
    
    return true;  // Keep the message channel open for sendResponse
  });
