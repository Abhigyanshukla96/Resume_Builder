const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const signinSaveBtn = document.getElementById('signin-btn');
const signupSaveBtn = document.getElementById('signup-btn');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

signupSaveBtn.addEventListener('click', (e) => {
	e.preventDefault();
	const username = document.getElementById('signup-username').value;
	const password = document.getElementById('signup-password').value;
	const email = document.getElementById('signup-email').value;

	let payload = {
		method:'POST',
		headers:{
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'username': username,
			'email': email,
			'password': password
		})
	};

	fetch('signup/', payload)
	.then(response => response.json())
	.then(res => {
		if(!res.error){
			console.log(res);
			container.classList.remove("right-panel-active");		
		}
	})
});

signinSaveBtn.addEventListener('click', (e) => {
	e.preventDefault();
	const username = document.getElementById('signin-username').value;
	const password = document.getElementById('signin-password').value;

	let payload = {
		method:'POST',
		headers:{
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'username': username,
			'password': password
		})
	};

	fetch('signin/', payload)
	.then(response => response.json())
	.then(res => {
		if(!res.error){
			console.log(res);
			container.classList.remove("right-panel-active");		
		}
	})
});