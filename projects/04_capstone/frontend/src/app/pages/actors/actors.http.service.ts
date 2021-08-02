import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Actor } from './actors.interface';

@Injectable({ providedIn: 'root' })
export class ActorsHttpService extends BaseHttpService {
    endpoint: string = 'actors';

    constructor(private http: HttpClient) {
        super();
    }

    getAll(): Observable<Actor[]> {
        return this.http.get<Actor[]>(this.endpoint).pipe(retry(1), catchError(this.handleError));
    }
}