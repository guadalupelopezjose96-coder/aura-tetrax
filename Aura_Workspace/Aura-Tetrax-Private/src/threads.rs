// PROPRIETARY AND CONFIDENTIAL
// Copyright (C) 2026 JEGL. All Rights Reserved.
// This software is proprietary commercial asset distributed privately.
// Unauthorized copying, distribution, or alteration is strictly prohibited.
// Verification of license required for execution.
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;
use std::thread;
use std::hint;

#[repr(align(64))]
pub struct CoreWorker {
    pub core_id: usize,
    pub is_active: AtomicBool,
}

pub struct AuraThreadPool {
    workers: Vec<Arc<CoreWorker>>,
    handles: Vec<thread::JoinHandle<()>>,
}

impl AuraThreadPool {
    pub fn new(total_cores: usize, reserve_cores: usize) -> Self {
        let execution_cores = total_cores.saturating_sub(reserve_cores);
        let mut workers = Vec::with_capacity(execution_cores);
        let mut handles = Vec::with_capacity(execution_cores);

        println!(
            "[INFO] Inicializando Pool de Alto Rendimiento. Cores totales: {}, Asignados: {}, Reservados: {}",
            total_cores, execution_cores, reserve_cores
        );

        for core_id in 0..execution_cores {
            let worker = Arc::new(CoreWorker {
                core_id,
                is_active: AtomicBool::new(true),
            });
            workers.push(Arc::clone(&worker));

            let worker_clone = Arc::clone(&worker);
            let handle = thread::spawn(move || {
                while worker_clone.is_active.load(Ordering::Relaxed) {
                    hint::spin_loop();
                }
            });
            handles.push(handle);
        }

        Self { workers, handles }
    }

    pub fn shutdown(self) {
        for worker in &self.workers {
            worker.is_active.store(false, Ordering::Relaxed);
        }
        for handle in self.handles {
            let _ = handle.join();
        }
        println!("[INFO] Pool de procesamiento masivo detenido de forma segura y legal.");
    }
}
