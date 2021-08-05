import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-not-found',
  template: '<h1 fxLayoutAlign="center">Page is not found</h1>',
})
export class NotFoundComponent implements OnInit {
  constructor() { }

  ngOnInit(): void {
  }
}
