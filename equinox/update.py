import jax.tree_util as jtu
from jaxtyping import PyTree


def _apply_update(u, p):
    return p if u is None else p + u


def _is_none(x):
    return x is None


def apply_updates(model: PyTree, updates: PyTree) -> PyTree:
    """A `jtu.tree_map`-broadcasted version of
    ```python
    model = model if update is None else model + update
    ```

    This is often useful when updating a model's parameters via stochastic gradient
    descent. (This function is essentially the same as `optax.apply_updates`, except
    that it understands `None`.)

    **Arguments:**

    - `model`: An arbitrary PyTree.
    - `updates`: Any PyTree that is a prefix of `model`.

    **Returns:**

    The updated model.
    """
    # Assumes that updates is a prefix of model
    return jtu.tree_map(_apply_update, updates, model, is_leaf=_is_none)
