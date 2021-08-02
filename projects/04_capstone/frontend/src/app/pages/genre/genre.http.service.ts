import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Genre } from './genre.interface';

@Injectable({ providedIn: 'root' })
export class GenreHttpService extends BaseHttpService {
    endpoint: string = 'genres';

    constructor(private http: HttpClient) {
        super();
    }

    getById(id: number): Observable<Genre> {
        return this.http.get<Genre>(`${this.endpoint}/${id}`).pipe(retry(1), catchError(this.handleError));
    }
}