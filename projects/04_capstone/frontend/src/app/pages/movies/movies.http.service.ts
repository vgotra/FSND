import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Movies } from './movies.interface';

@Injectable({ providedIn: 'root' })
export class MoviesHttpService extends BaseHttpService {
    endpoint: string = '/api/movies';

    constructor(private http: HttpClient) {
        super();
    }

    getAll(): Observable<Movies> {
        return this.http.get<Movies>(this.endpoint).pipe(retry(1), catchError(this.handleError));
    }
}