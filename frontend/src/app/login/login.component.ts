import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  login() {
    if (this.username && this.password) {
      console.log("Username: " + this.username + ", Password: " + this.password);
    } else {
      console.error("Username and password required");
    }
  }
}

