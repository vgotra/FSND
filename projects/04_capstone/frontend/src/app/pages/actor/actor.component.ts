import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { ActorStoreService } from './actor.store.service';

@Component({
  selector: 'app-actor',
  templateUrl: './actor.component.html',
  styleUrls: ['./actor.component.scss']
})
export class ActorComponent implements OnInit, OnDestroy {
  subscription = new Subscription();

  constructor(public service: ActorStoreService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.subscription.add(this.route.params.pipe(
      switchMap((params) => this.service.LoadEntity(params['id']))
    ).subscribe());
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
