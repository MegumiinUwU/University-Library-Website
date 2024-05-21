document.getElementById('password').addEventListener('input', function () {
    const password = this.value;
    const confirm_password = document.getElementById('confirm_password');
  
    if (password !== confirm_password.value) {
      confirm_password.setCustomValidity('Passwords do not match');
    } else {
      confirm_password.setCustomValidity('');
    }
  });
  
  document.getElementById('confirm_password').addEventListener('input', function () {
    const password = document.getElementById('password').value;
    const confirm_password = this.value;
  
    if (password !== confirm_password) {
      this.setCustomValidity('Passwords do not match');
    } else {
      this.setCustomValidity('');
    }
  });