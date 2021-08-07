import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Subscription } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Genre } from '../genre/genre.interface';
import { GenresStoreService } from './genres.store.service';

@Component({
  selector: 'app-genres',
  templateUrl: './genres.component.html',
  styleUrls: ['./genres.component.scss']
})
export class GenresComponent implements OnInit, AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name'];
  dataSource: MatTableDataSource<Genre> = new MatTableDataSource<Genre>();
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  subscription = new Subscription();

  constructor(public service: GenresStoreService) { }

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
