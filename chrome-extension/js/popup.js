document.getElementById('postForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const platform = document.getElementById('platform').value;
    const action = document.getElementById('action').value;
    const content = document.getElementById('content').value;

    chrome.runtime.sendMessage({
      platform: platform,
      action: action,
      content: content
    }, function(response) {
      console.log('Response:', response);
    });
  });
