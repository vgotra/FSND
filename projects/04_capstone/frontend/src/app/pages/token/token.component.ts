import { Component, OnDestroy, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-token',
  templateUrl: './token.component.html',
  styleUrls: ['./token.component.scss']
})
export class TokenComponent implements OnInit, OnDestroy {
  subscription = new Subscription();

  token:string | undefined;

  constructor(private auth: AuthService) { }

  ngOnInit(): void {
    this.subscription.add(this.auth.getAccessTokenSilently().subscribe(x => this.token = x))
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
