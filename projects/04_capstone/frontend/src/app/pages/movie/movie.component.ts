import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { MovieStoreService } from './movie.store.service';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.scss']
})
export class MovieComponent implements OnInit, OnDestroy {
  subscription = new Subscription();

  constructor(public service: MovieStoreService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscription.add(this.route.params.pipe(
      switchMap((params) => this.service.LoadEntity(params['id']))
    ).subscribe());
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
