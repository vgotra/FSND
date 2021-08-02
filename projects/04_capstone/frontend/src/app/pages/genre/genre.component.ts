import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { GenreStoreService } from './genre.store.service';

@Component({
  selector: 'app-genre',
  templateUrl: './genre.component.html',
  styleUrls: ['./genre.component.scss']
})
export class GenreComponent implements OnInit, OnDestroy {
  subscription = new Subscription();

  constructor(public service: GenreStoreService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscription.add(this.route.params.pipe(
      switchMap((params) => this.service.LoadEntity(params['id']))
    ).subscribe());
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
