import { useCallback, useState } from "react";

interface UseConfirmDeleteOptions<TId> {
  onDelete: (id: TId) => Promise<void>;
}

interface UseConfirmDeleteResult<TId> {
  cancel: () => void;
  confirm: () => Promise<void>;
  isDeleting: boolean;
  isOpen: boolean;
  pendingId: TId | null;
  requestDelete: (id: TId) => void;
}

/**
 * Manages the confirm-then-delete flow for a single deletable entity.
 *
 * `requestDelete(id)` opens the confirmation and records the pending id.
 * `cancel()` dismisses without deleting. `confirm()` runs `onDelete(pendingId)`,
 * tracking `isDeleting`, and always clears state afterwards.
 */
export function useConfirmDelete<TId>({
  onDelete,
}: UseConfirmDeleteOptions<TId>): Readonly<UseConfirmDeleteResult<TId>> {
  const [pendingId, setPendingId] = useState<TId | null>(null);
  const [isOpen, setIsOpen] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  const requestDelete = useCallback((id: TId) => {
    setPendingId(id);
    setIsOpen(true);
  }, []);

  const cancel = useCallback(() => {
    setIsOpen(false);
    setPendingId(null);
  }, []);

  const confirm = useCallback(async () => {
    if (pendingId === null) return;
    setIsDeleting(true);
    try {
      await onDelete(pendingId);
    } finally {
      setIsDeleting(false);
      setIsOpen(false);
      setPendingId(null);
    }
  }, [onDelete, pendingId]);

  return {
    cancel,
    confirm,
    isDeleting,
    isOpen,
    pendingId,
    requestDelete,
  } as const;
}
