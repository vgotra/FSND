import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Languages } from './languages.interface';

@Injectable({ providedIn: 'root' })
export class LanguagesHttpService extends BaseHttpService {
    endpoint: string = 'languages';

    constructor(private http: HttpClient) {
        super();
    }

    getAll(): Observable<Languages> {
        return this.http.get<Languages>(this.endpoint).pipe(retry(1), catchError(this.handleError));
    }
}