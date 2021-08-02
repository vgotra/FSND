import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Subscription } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Language } from './languages.interface';
import { LanguagesStoreService } from './languages.store.service';

@Component({
  selector: 'app-languages',
  templateUrl: './languages.component.html',
  styleUrls: ['./languages.component.scss']
})
export class LanguagesComponent implements OnInit, AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name'];
  dataSource: MatTableDataSource<Language> = new MatTableDataSource<Language>();
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  subscription = new Subscription();

  constructor(public service: LanguagesStoreService) { }

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
