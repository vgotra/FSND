import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Subscription } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Actor } from './actors.interface';
import { ActorsStoreService } from './actors.store.service';

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.scss']
})
export class ActorsComponent implements OnInit, AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name', 'birthday', 'sex', 'profileUrl', 'photoUrl'];
  dataSource: MatTableDataSource<Actor> = new MatTableDataSource<Actor>();
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  subscription = new Subscription();

  constructor(public service: ActorsStoreService) { }

  ngOnInit(): void {
    this.subscription.add(this.service.LoadEntities().pipe(
      tap(() => this.service.entities$.subscribe(entities => this.dataSource.data = entities))
    ).subscribe());
  }

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
