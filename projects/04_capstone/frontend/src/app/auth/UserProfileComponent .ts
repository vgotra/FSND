import { Component } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Component({
    selector: 'app-user-profile',
    template: `
    <ng-container *ngIf="auth.user$ | async as user">
      <h1>{{ user.nickname }}</h1>
    </ng-container>`
})
export class UserProfileComponent {
    constructor(public auth: AuthService) { }
}