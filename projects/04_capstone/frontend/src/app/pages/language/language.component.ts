import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { LanguageStoreService } from './language.store.service';

@Component({
  selector: 'app-language',
  templateUrl: './language.component.html',
  styleUrls: ['./language.component.scss']
})
export class LanguageComponent implements OnInit, OnDestroy {
  subscription = new Subscription();

  constructor(public service: LanguageStoreService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscription.add(this.route.params.pipe(
      switchMap((params) => this.service.LoadEntity(params['id']))
    ).subscribe());
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
