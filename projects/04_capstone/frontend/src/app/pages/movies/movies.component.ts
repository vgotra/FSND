import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Subscription } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Movie } from './movies.interface';
import { MoviesStoreService } from './movies.store.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit, AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name', 'description', 'releaseDate', 'releaseCountry'];
  dataSource: MatTableDataSource<Movie> = new MatTableDataSource<Movie>();
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  subscription = new Subscription();

  constructor(public service: MoviesStoreService) { }

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
